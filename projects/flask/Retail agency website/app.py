import os
from flask import Flask, render_template, request, abort, jsonify, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import sys
from database.models import setup_db, db, House, Agent, Job
from auth.auth import requires_auth, AuthError
import json
import http


def create_app(test_config=None):

    login_url = os.environ.get("LOGIN_URL")

    app = Flask(__name__)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    setup_db(app)
    CORS(app)

    # ====================FRONTEND ENDPOINTS=========================
    # BACKEND API CODE STARTS AT LINE 133

    @app.route('/')
    def home():
        houses = House.query.order_by(House.id.desc()).limit(3)
        houses = [house.format() for house in houses]
        agents = Agent.query.order_by(Agent.id.desc()).limit(4)
        agents = [agent.format() for agent in agents]
        data = {
            'houses': houses,
            'agents': agents
        }
        return render_template('index.html', data=data)

    @app.route('/agents')
    def agents_holder():
        return render_template('agents.html', data='')

    @app.route('/agents/create', methods=['GET'])
    def create_agent_form():
        return render_template('forms/new-agent.html')

    @app.route('/agents/update/<id>', methods=['GET'])
    def update_agent_form(id):
        agent = Agent.query.filter(Agent.id == id).one_or_none()
        return render_template('forms/update-agent.html', data=agent.format())

    @app.route('/agents.html')
    @requires_auth('get:agents')
    def agents(permission):
        agents = get_agents()
        return render_template('agents.html', data=agents.json)

    @app.route('/agents-details/<id>')
    def agents_details_holder(id):
        return render_template('agents-details.html', data=jsonify({'id': id}).json)

    @app.route('/agents-details.html/<id>')
    @requires_auth('get:agents')
    def agents_details(permission, id):
        agent = get_agent(id)
        return render_template('agents-details.html', data=agent.json)

    @app.route('/properties')
    def properties_holder():
        return render_template('properties.html', data='')

    @app.route('/properties.html')
    @requires_auth('get:houses')
    def properties(permission):
        houses = get_houses()
        return render_template('properties.html', data=houses.json)

    @app.route('/properties/create', methods=['GET'])
    def create_property_form():
        return render_template('forms/new-property.html')

    @app.route('/properties/update/<id>', methods=['GET'])
    def update_property_form(id):
        house = House.query.filter(House.id == id).one_or_none()
        return render_template('forms/update-property.html', data=house.format())

    @app.route('/properties-details/<id>')
    def properties_details_holder(id):
        return render_template('properties-details.html', data=jsonify({'id': id}).json)

    @app.route('/properties-details.html/<id>')
    @requires_auth('get:houses')
    def properties_details(permission, id):
        house = get_house(id)
        return render_template('properties-details.html', data=house.json)

    @app.route('/contact.html')
    def contact():
        return render_template('contact.html')

    @app.route('/jobs')
    def jobs_holder():
        return render_template('jobs.html', data='')

    @app.route('/jobs.html')
    @requires_auth('get:jobs')
    def jobs(permission):
        jobs = get_jobs()
        return render_template('jobs.html', data=jobs.json)

    @app.route('/jobs/create', methods=['GET'])
    def create_job_form():
        return render_template('forms/new-job.html')

    @app.route('/jobs/update/<agent_id>&<house_id>', methods=['GET'])
    def update_job_form(agent_id, house_id):
        job = Job.query.filter(
            Job.agent_id == agent_id and Job.house_id == house_id).one_or_none()
        return render_template('forms/update-job.html', data=job.format())

    @app.route('/jobs-details/<agent_id>&<house_id>')
    def jobs_details_holder(agent_id, house_id):
        return render_template('jobs-details.html', data=jsonify({'agent_id': agent_id, 'house_id': house_id}).json)

    @app.route('/jobs-details.html/<agent_id>&<house_id>')
    @requires_auth('get:jobs')
    def jobs_details(permission, agent_id, house_id):
        job = get_job(agent_id, house_id)
        return render_template('jobs-details.html', data=job.json)

    @app.route('/login')
    def login():
        return redirect(login_url)

    # ================== Agents Endpoints =====================
    @app.route('/get-agents')
    @requires_auth('get:agents')
    def get_agents(permission):
        agents = Agent.query.order_by(Agent.id.desc()).all()
        formatted_agents = [agent.format() for agent in agents]
        return jsonify({
            "success": True,
            "agents": formatted_agents
        })

    @app.route('/get-agent/<id>')
    @requires_auth('get:agents')
    def get_agent(permission, id):
        selected_agent = Agent.query.filter(Agent.id == id).one_or_none()
        if(selected_agent is None):
            return not_found(404)
        else:
            return jsonify({
                "success": True,
                "agents": selected_agent.format()
            })

    @app.route('/create-agent', methods=['POST'])
    @requires_auth('post:agents')
    def create_agent(permission):
        body = request.get_json()
        try:
            person = Agent(name=body.get('name', ''),
                           age=body.get('age', ''), picture='')
            person.insert()
        except:
            print(sys.exc_info())
            db.session.rollback()
            return unprocessable(422)
        return get_agents()

    @app.route('/update-agent/<id>', methods=['PUT'])
    @requires_auth('put:agents')
    def update_agent(permission, id):
        selected_agent = Agent.query.filter(Agent.id == id).one_or_none()
        if selected_agent is None:
            return not_found(404)
        else:
            body = request.get_json()
            name = body.get('name', selected_agent.name)
            age = body.get('age', selected_agent.age)
            picture = body.get('picture', selected_agent.picture)
            try:
                selected_agent.name = name
                selected_agent.age = age
                selected_agent.picture = picture
                selected_agent.update()
            except:
                print(sys.exc_info())
                db.session.rollback()
                return unprocessable(422)
            return get_agents()

    @app.route('/delete-agent/<id>', methods=['DELETE'])
    @requires_auth('delete:agents')
    def delete_agent(permission, id):
        selected_agent = Agent.query.filter(Agent.id == id).one_or_none()
        if selected_agent is None:
            return not_found(404)
        else:
            try:
                selected_agent.delete()
            except:
                print(sys.exc_info())
                db.session.rollback()
                return unprocessable(422)
            return get_agents()

    # ================== Houses Endpoints =====================
    @app.route('/get-houses')
    @requires_auth('get:houses')
    def get_houses(permission):
        houses = House.query.order_by(House.id.desc()).all()
        formatted_houses = [house.format() for house in houses]
        return jsonify({
            "success": True,
            "houses": formatted_houses
        })

    @app.route('/get-house/<id>')
    @requires_auth('get:houses')
    def get_house(permission, id):
        selected_house = House.query.filter(House.id == id).one_or_none()
        if(selected_house is None):
            return not_found(404)
        else:
            return jsonify({
                "success": True,
                "house": selected_house.format()
            })

    @app.route('/create-house', methods=['POST'])
    @requires_auth('post:houses')
    def create_house(permission):
        body = request.get_json()
        try:
            house = House(
                name=body.get('name', ''),
                rooms=body.get('rooms', ''),
                price=body.get('price', ''),
                picture=body.get('picture', ''))
            house.insert()
        except:
            print(sys.exc_info())
            db.session.rollback()
            return unprocessable(422)
        return get_houses()

    @app.route('/update-house/<id>', methods=['PUT'])
    @requires_auth('put:houses')
    def update_house(permission, id):
        selected_house = House.query.filter(House.id == id).one_or_none()
        if selected_house is None:
            return not_found(404)
        else:
            body = request.get_json()
            name = body.get('name', selected_house.name)
            rooms = body.get('rooms', selected_house.rooms)
            price = body.get('price', selected_house.price)
            picture = body.get('picture', selected_house.picture)
            try:
                selected_house.name = name
                selected_house.rooms = rooms
                selected_house.price = price
                selected_house.picture = picture
                selected_house.update()
            except:
                print(sys.exc_info())
                db.session.rollback()
                return unprocessable(422)
            return get_houses()

    @app.route('/delete-house/<id>', methods=['DELETE'])
    @requires_auth('delete:houses')
    def delete_house(permission, id):
        selected_house = House.query.filter(House.id == id).one_or_none()
        if selected_house is None:
            return not_found(404)
        else:
            try:
                selected_house.delete()
            except:
                print(sys.exc_info())
                db.session.rollback()
                return unprocessable(422)
            return get_houses()

    # ================== Jobs Endpoints =====================
    @app.route('/get-jobs')
    @requires_auth('get:jobs')
    def get_jobs(permission):
        jobs = Job.query.order_by(Job.agent_id.desc()).all()
        formatted_jobs = [job.format() for job in jobs]
        return jsonify({
            "success": True,
            "jobs": formatted_jobs
        })

    @app.route('/get-job/<agent_id>&<house_id>')
    @requires_auth('get:jobs')
    def get_job(permission, agent_id, house_id):
        selected_job = Job.query.filter(
            Job.agent_id == agent_id and Job.house_id == house_id).one_or_none()
        if(selected_job is None):
            return not_found(404)
        else:
            return jsonify({
                "success": True,
                "job": selected_job.format()
            })

    @app.route('/create-job', methods=['POST'])
    @requires_auth('post:jobs')
    def create_job(permission):
        body = request.get_json()
        try:
            job = Job(
                agent_id=body.get('agent_id', ''),
                house_id=body.get('house_id', ''),
            )
            job.insert()
        except:
            print(sys.exc_info())
            db.session.rollback()
            return unprocessable(422)
        return get_jobs()

    @app.route('/update-job/<agent_id>&<house_id>', methods=['PUT'])
    @requires_auth('put:jobs')
    def update_job(permission, agent_id, house_id):
        selected_job = Job.query.filter(
            Job.agent_id == agent_id and Job.house_id == house_id).one_or_none()
        if selected_job is None:
            return not_found(404)
        else:
            body = request.get_json()
            agent_id = body.get('agent_id', '-1'),
            house_id = body.get('house_id', '-1'),
            try:
                selected_job.agent_id = agent_id
                selected_job.house_id = house_id
                selected_job.update()
            except:
                print(sys.exc_info())
                db.session.rollback()
                return unprocessable(422)
            return get_jobs()

    @app.route('/delete-job/<agent_id>&<house_id>', methods=['DELETE'])
    @requires_auth('delete:jobs')
    def delete_job(permission, agent_id, house_id):
        selected_job = Job.query.filter(
            Job.agent_id == agent_id and Job.house_id == house_id).one_or_none()

        if selected_job is None:
            return not_found(404)
        else:
            try:
                selected_job.delete()
            except:
                print(sys.exc_info())
                db.session.rollback()
                return unprocessable(422)
            return get_jobs()

    #=================ERROR HANDLERS==================#
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "You don't have the permission to access the requested resource."
        }), 403

    @app.errorhandler(405)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error, check logs for more details"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authorization header is expected."
        }), 401
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
