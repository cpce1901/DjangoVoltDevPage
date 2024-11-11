/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../static/**/*.js'
  ],
  theme: {
    extend: {
      backgroundImage:{
        "main": "url('/static/img/esp-32.jpg')",
      },
      fontFamily: {
        "exo": ['"exo 2"'],
        "rale": ['"Raleway"'],
      },
    },
  },
  plugins: [],
}

