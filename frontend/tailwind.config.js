/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Primära färger från vår färgpalett
        primary: {
          blue: "#1E90FF",
          darkBlue: "#0B3D91",
        },
        // Sekundära färger
        secondary: {
          lightGray: "#F5F5F5",
          gray: "#B0B0B0",
        },
        // Accentfärger
        accent: {
          green: "#32CD32",
          red: "#FF4500",
          yellow: "#FFD700",
        },
        // Stödfärger
        neutral: {
          white: "#FFFFFF",
          black: "#000000",
        },
      },
    },
  },
  plugins: [],
} 