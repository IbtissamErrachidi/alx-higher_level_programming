#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

// Vérifier si le chemin du fichier est fourni en argument
if (!file) {
  console.error('Usage: node 0-readme.js <file>');
  process.exit(1);
}

// Lire le contenu du fichier en utilisant l'encodage UTF-8
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    // Si une erreur survient, afficher l'objet d'erreur
    console.error(err);
  } else {
    // Si la lecture réussit, imprimer le contenu du fichier
    console.log(data);
  }
});
