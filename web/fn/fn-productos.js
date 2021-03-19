$scope.arrProductos = [];
$scope.findProductos = function () {
	$scope.cargando = false;
	$.ajax({
		url: "../../findProductos",
		data: {},
		beforeSend: function (xhr) {
			$scope.cargandoProductos = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.arrProductos = resultado;
			$scope.cargandoProductos = false;
			$scope.$evalAsync();
		},
	});
};
