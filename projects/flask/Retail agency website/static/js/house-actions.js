$(document).ready(function () {
    var create_form = document.getElementById('property-creation-form');
    if (create_form != null) {
        create_form.onsubmit = function (e) {
            e.preventDefault();
            fetch('/create-house', {
                method: 'POST',
                body: JSON.stringify({
                    'name': document.getElementById('name').value,
                    'rooms': document.getElementById('rooms').value,
                    'price': document.getElementById('price').value,
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
                    window.location.href = "/properties";
                }
            }).catch(function () {
                alert('Error');
            })
        }
    }
    var update_form = document.getElementById('property-update-form');

    if (update_form != null) {
        update_form.onsubmit = function (e) {
            e.preventDefault();
            fetch('/update-house/' + update_form.dataset['id'], {
                method: 'PUT',
                body: JSON.stringify({
                    'name': document.getElementById('name').value,
                    'rooms': document.getElementById('rooms').value,
                    'price': document.getElementById('price').value,
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
                    window.location.href = "/properties";
                }
            }).catch(function () {
                alert('Error');
            })
        }
    }
});

function delete_property(id) {
    fetch('/delete-house/' +id, {
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
            window.location.href = "/properties";
        }
    }).catch(function () {
        alert('Error');
    });

}