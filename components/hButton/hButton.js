(function() {
    // Create the button element
    const button = document.createElement('button');
    button.innerText = 'Click Me!';
    button.id = 'hbutton';  // Set a unique ID for the button

    // Append the button to the body of the page
    document.body.appendChild(button);

    // Add click event handler
    button.addEventListener('click', function() {
        alert('Button was clicked!');
    });
})();