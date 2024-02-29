/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "white": "#FFFFFF",
        "green": "#09A129",
        "yellow": "#FAF33E",
        "red": "#C1292E",
        "purple": "#7EFF8F",
      },
      animation: {
        'rotate': 'rotate 3s linear infinite',
      }
    },
    
  },
  plugins: [],
}
