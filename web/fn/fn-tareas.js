$scope.findTareas = function () {
	$.ajax({
		url: "../../findTareas",
		data: {},
		beforeSend: function (xhr) {
			$scope.arrTareas = [];
			$scope.cargandoTareas = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.arrTareas = resultado;
			$scope.cargandoTareas = false;
			$scope.$evalAsync();
		},
	});
};
