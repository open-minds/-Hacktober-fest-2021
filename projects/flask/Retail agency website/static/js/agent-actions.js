$(document).ready(function () {
    var create_form = document.getElementById('agent-creation-form');
    if (create_form != null) {
        create_form.onsubmit = function (e) {
            e.preventDefault();
            fetch('/create-agent', {
                method: 'POST',
                body: JSON.stringify({
                    'name': document.getElementById('name').value,
                    'age': document.getElementById('age').value,
                    'picture': document.getElementById('picture').value
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
                    window.location.href = "/agents";
                }
            }).catch(function () {
                alert('Error');
            })
        }
    }
    var update_form = document.getElementById('agent-update-form');

    if (update_form != null) {
        update_form.onsubmit = function (e) {
            e.preventDefault();
            fetch('/update-agent/' + update_form.dataset['id'], {
                method: 'PUT',
                body: JSON.stringify({
                    'name': document.getElementById('name').value,
                    'age': document.getElementById('age').value,
                    'picture': document.getElementById('picture').value
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
                    window.location.href = "/agents";
                }
            }).catch(function () {
                alert('Error');
            })
        }
    }
});

function delete_agent(id) {
    fetch('/delete-agent/' +id, {
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
            window.location.href = "/agents";
        }
    }).catch(function () {
        alert('Error');
    });

}