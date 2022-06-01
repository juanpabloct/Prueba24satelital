//Prueba desarrollada con javaScript
// Documentacion: https://developer.mozilla.org/es/docs/Web/JavaScrip

function Espejo(matriz) {
  var matrizEspejo = [];
  var longitudMatriz = matriz.length - 1;
  //iteracion para recorrer la matriz al reves
  while (longitudMatriz != 0) {
    matrizEspejo.push(matriz[longitudMatriz]);
    longitudMatriz--;
  }
  return `Matriz original: ${matriz},  Matriz Espejo:${matrizEspejo}`;
}
console.log(Espejo(["a", "b", "c", "d", "e"]));

//Ejecucion: node matrizEspejo.js
