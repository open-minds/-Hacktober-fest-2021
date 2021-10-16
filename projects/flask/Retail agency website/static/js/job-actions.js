$(document).ready(function () {
    var create_form = document.getElementById('job-creation-form');
    if (create_form != null) {
        create_form.onsubmit = function (e) {
            e.preventDefault();
            fetch('/create-job', {
                method: 'POST',
                body: JSON.stringify({
                    'agent_id': document.getElementById('agent_id').value,
                    'house_id': document.getElementById('house_id').value
                }),
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + window.localStorage.getItem('access_token'),
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': '*'
                }
            }).then(function (response) {
                return response.json();
            }).then(function (jsonResponse) {
                console.log(jsonResponse);
                console.log(jsonResponse['success']);
                if (jsonResponse['success'] == true) {
                    window.location.href = "/jobs";
                }
            }).catch(function () {
                alert('Error');
            })
        }
    }
    var update_form = document.getElementById('job-update-form');

    if (update_form != null) {
        update_form.onsubmit = function (e) {
            e.preventDefault();
            fetch('/update-job/' + update_form.dataset['agent']+'&'+update_form.dataset['house'], {
                method: 'PUT',
                body: JSON.stringify({
                    'agent_id': document.getElementById('agent_id').value,
                    'house_id': document.getElementById('house_id').value
                }),
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + window.localStorage.getItem('access_token'),
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': '*'
                }
            }).then(function (response) {
                return response.json();
            }).then(function (jsonResponse) {
                console.log(jsonResponse);
                console.log(jsonResponse['success']);
                if (jsonResponse['success'] == true) {
                    window.location.href = "/jobs";
                }
            }).catch(function () {
                alert('Error');
            })
        }
    }
});

function delete_job(agent_id, house_id) {
    fetch('/delete-job/' +agent_id+'&'+house_id, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.localStorage.getItem('access_token'),
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*'
        }
    }).then(function (response) {
        return response.json();
    }).then(function (jsonResponse) {
        console.log(jsonResponse);
        console.log(jsonResponse['success']);
        if (jsonResponse['success'] == true) {
            window.location.href = "/jobs";
        }
    }).catch(function () {
        alert('Error');
    });

}