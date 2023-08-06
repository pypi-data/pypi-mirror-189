#  TP1 Exercice 8

## Objectif 
L'objectif de cet exercice est de creer une version zippé de notre projet

## Realisation 
J'ai créé deux packages, un permettant de stocker le script de SimpleComplexCalculator et un autre package contenant un script de test. J'ai initialisé un fichier setup.py afin d'archiver le fichier Package_Calculator

## Organisation
voici l'arborescence de notre projet :
```
.
├── Package_Calculator
│   ├── Calculator.py
│   ├── __init__.py
│   └── TestSimpleComplexCalculator.egg-info
│       
├── Package_Test
│   ├── exo7.py
│   └── __init__.py
│
├── dist
│   ├── TestSimpleComplexCalculator-0.0.1.tar.gz
│   └── TestSimpleComplexCalculator-0.0.1-py3-none-any.whl
│
├── setup.py
│
└── README.md
```


## Lancement
on exécute la commande :
  
```
python3 -m build
```




