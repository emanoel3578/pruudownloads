module.exports = {
  purge: { content: ['./public/**/*.html', './src/**/*.vue'] },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily:{
        kanit: ["Kanit"],
        fjalla: ["Fjalla One"],
        poppins: ["Poppins"]
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
