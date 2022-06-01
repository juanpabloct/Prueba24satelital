//Prueba desarrollada con javaScript
// Documentacion: https://developer.mozilla.org/es/docs/Web/JavaScrip

function RotacionMatriz(matriz) {
  var matrizEspejo = "";
  var longitudMatriz = matriz.length - 1;
  while (longitudMatriz >= 0) {
    matrizEspejo += matriz[longitudMatriz];
    longitudMatriz--;
  }
  return `Matriz original: ${matriz},  Rotacion Matriz:${matrizEspejo}`;
}
console.log(RotacionMatriz("mxn"));

//Ejecucion: node matrizEspejo.js
