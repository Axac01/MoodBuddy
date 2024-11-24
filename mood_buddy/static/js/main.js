// Array of image file names
const images = [
    '/static/images/image1.svg', // First image
    '/static/images/image2.png', // Second image
    '/static/images/image3.svg'  // Add more images as needed
];

let currentIndex = 0; // Track the current image index

// Reference to the image element
const svgImage = document.getElementById('svg-image');

// Reference to the button
const changeImageButton = document.getElementById('change-image-button');

// Change Image on Button Click
changeImageButton.addEventListener('click', () => {
    // Update the index
    currentIndex = (currentIndex + 1) % images.length; // Loop back to first image after the last

    // Update the src of the image
    svgImage.src = images[currentIndex];
});

