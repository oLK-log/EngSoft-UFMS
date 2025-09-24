#include "poligonos.h"

float calcPerimetroTriangulo(float a, float b, float c){
    return a+b+c;
}

float calcPerimetroRetangulo(float b, float a){
    return 2*a + 2*b;
}

float calcPerimetroCirculo(float r){
    return 2*PI*r;
}

float calcAreaTriangulo(float a, float h){
    return (a*h)/2;
}

float calcAreaRetangulo(float a, float b){
    return a*b;
}

float calcAreaCirculo(float r){
    return PI*r*r;
}
