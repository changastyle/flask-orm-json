$('#cont-mid-menus').scroll(function() 
{
    var desplazamientoActual = $(this).scrollLeft();
    var alturaPadre = $(this).width();
    var alturaTotal = $('#scrolleador-verdadero-cont-mid-menus').innerWidth();

    console.log("DESPLAZAMIENTO ACTUAL " + desplazamientoActual);
    console.log("ALTURA PADRE: " + alturaPadre);
    console.log("alturaTotal " + alturaTotal);

    // Current percentual position
    $scope.porcentajeScrollLateral = parseInt((desplazamientoActual / (alturaTotal - alturaPadre)) * 100);
    $scope.$evalAsync();

    console.log("$scope.porcentajeScrollLateral: " + $scope.porcentajeScrollLateral);
});

$scope.porcentajeScrollLateral  = 0;
$scope.scrollMenusMidLateral = function(direccion)
{
    var desplazamientoActual =  $('#cont-mid-menus').scrollLeft();
    var alturaPadre =  $('#cont-mid-menus').width();
    var alturaTotal = $('#scrolleador-verdadero-cont-mid-menus').innerWidth();

    console.log("DESPLAZAMIENTO ACTUAL " + desplazamientoActual);
    console.log("ALTURA PADRE: " + alturaPadre);
    console.log("alturaTotal " + alturaTotal);

    // Current percentual position
    $scope.porcentajeScrollLateral = parseInt((desplazamientoActual / (alturaTotal - alturaPadre)) * 100);

    console.log("$scope.porcentajeScrollLateral: " + $scope.porcentajeScrollLateral);


    if(direccion == 'der')
    {
        incremento = 150;
    }
    else
    {
        incremento = -150; 
    }

    // REAL SCROLL:
    $('#cont-mid-menus').animate(
    {
        scrollLeft: "+=" + incremento
    }, 500);

    $scope.$evalAsync();

}