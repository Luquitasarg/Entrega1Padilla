/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
let cursos = 0;
let estudiantes = 0;
let profesores = 0;

function despliegaCursos(){
    if (cursos == 0)
    {
        document.getElementById('listaCursos').style.display = "block";
        document.getElementById('listaEstudiantes').style.display = "none";
        document.getElementById('listaProfesores').style.display = "none";
        cursos = 1;
        estudiantes = 0;
        profesores = 0;
    }
    else
    {
        document.getElementById('listaCursos').style.display = "none";
        cursos = 0;
    }
}

function despliegaEstudiantes(){
    if (estudiantes == 0)
    {
        document.getElementById('listaEstudiantes').style.display = "block";
        document.getElementById('listaCursos').style.display = "none";
        document.getElementById('listaProfesores').style.display = "none";
        estudiantes = 1;
        cursos = 0;
        profesores = 0;
    }
    else
    {
        document.getElementById('listaEstudiantes').style.display = "none";
        estudiantes = 0;
    }
}

function despliegaProfesores(){
    if (profesores == 0)
    {
        document.getElementById('listaProfesores').style.display = "block";
        document.getElementById('listaCursos').style.display = "none";
        document.getElementById('listaEstudiantes').style.display = "none";
        profesores = 1;
        cursos = 0;
        estudiantes = 0;
    }
    else
    {
        document.getElementById('listaProfesores').style.display = "none";
        profesores = 0;
    }
}