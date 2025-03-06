document.addEventListener('DOMContentLoaded', function() {
    // Select the container element
    const container = document.querySelector('.container');
    container.style.backgroundColor = 'lightblue';

    // Add a click event listener to the container
    container.addEventListener('click', function() {
        // Change the background color when the container is clicked
        container.style.backgroundColor = getRandomColor(); // You can define your color or use a function to generate a random color
    });

    // Function to generate a random color
    function getRandomColor() {
        const letters = '0123456789ABCDEF';  // A string of all possible hexadecimal characters (0-9, A-F)
        let color = '#';  // Start the color string with '#' (indicating a hex color in CSS)
    
        for (let i = 0; i < 6; i++) {  // Repeat the following block 6 times, as a hex color is 6 digits long
            // Randomly select one character from the 'letters' string (0-9 or A-F)
            color += letters[Math.floor(Math.random() * 16)]; //Multiplying by 16 gives a number between 0 and 16 (not inclusive of 16).
        }
    
        return color;  // Return the full hex color string (e.g., #3E7F9A)
    }
    
});
