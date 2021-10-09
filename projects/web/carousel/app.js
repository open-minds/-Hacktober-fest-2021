let arryofimages = [
    [
        './imgbg1.jpg',
        './imgbg2.jpg',
        './imgbg3.jpg'
    ],
    [
        './imgbg4.jpg',
        './imgbg5.jpg',
        './imgbg6.jpg'
    ],
    [
        './imgbg7.jpg',
        './imgbg8.jpg',
        './imgbg9.jpg'
    ],
    [
        './imgbg7.jpg',
        './imgbg8.jpg',
        './imgbg9.jpg'
    ]
]
function* forward(images) {
    for (let index = 0; index < images.length; index++) {
        const element = images[index];
        yield element
    }
}
function* backward(images) {
    let finalarry = images.reverse()
    for (let index = 0; index < finalarry.length; index++) {
        const element = finalarry[index];
        yield element
    }
}
let imageiteratorforward = forward(arryofimages)
let imageiteratorbackword = backward(arryofimages)
document.getElementById("forward").addEventListener("click", forwardbtn)
function forwardbtn() {
    const arry = imageiteratorforward.next().value
    let parent = document.getElementById('parent')
    let str = ``
    if (arry != undefined) {
        arry.forEach(element => {
            str += `<div class="carousel-card banner" style='background-image:url(${element})';>
            <div class="inner-carousel-card">
                <h2 style="align-self: flex-start;">web design</h2>
                <p class="display-6">Working Spaces for Startups Freelancer</p>
            </div>
        </div>`
        });
        parent.innerHTML = str
    } else {
        document.getElementById('forward').setAttribute('disabled', true)
        setTimeout(() => {
            window.location.reload()
        }, 2000);
    }
}
document.getElementById("backward").addEventListener("click", backwardbtn)
function backwardbtn() {
    const arry = imageiteratorbackword.next().value
    let parent = document.getElementById('parent')
    let str = ``
    if (arry != undefined) {
        arry.forEach(element => {
            str += `<div class="carousel-card banner" style='background-image:url(${element})';>
            <div class="inner-carousel-card">
                <h2 style="align-self: flex-start;">web design</h2>
                <p class="display-6">Working Spaces for Startups Freelancer</p>
            </div>
        </div>`
        });
        parent.innerHTML = str
    } else {
        document.getElementById('forward').setAttribute('disabled', true)
        setTimeout(() => {
            window.location.reload()
        }, 2000);
    }
}
