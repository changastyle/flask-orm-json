$scope.findPromos = function (soloActivos, soloXS) {
	console.log("findPromosByInstalacion");
	$.ajax({
		url: "../../findPromosByInstalacion",
		data: {
			soloActivos: soloActivos,
			soloXS: soloXS,
		},
		beforeSend: function (xhr) {
			$scope.cargandoPromos = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.arrPromos = resultado;
			$scope.cargandoPromos = false;
			$scope.$evalAsync();

			$(".carousel").carousel({
				interval: 4000,
			});
		},
	});
};
$scope.findPromosAllActivas = function (soloActivos, soloXS) {
	console.log("findPromosAllActivas");
	$.ajax({
		url: "../../findPromosAllActivas",
		beforeSend: function (xhr) {
			$scope.cargandoPromos = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.arrPromosLG = [];
			$scope.arrPromosXS = [];

			for (i = 0; i < resultado.length; i++) {
				promoLoop = resultado[i];

				if (promoLoop.xs) {
					$scope.arrPromosXS.push(promoLoop);
				} else {
					$scope.arrPromosLG.push(promoLoop);
				}
			}

			//            $scope.arrPromos = resultado;
			$scope.cargandoPromos = false;
			$scope.$evalAsync();

			$(".carousel").carousel({
				interval: 4000,
			});
		},
	});
};
$scope.getPromoEmpty = function () {
	console.log("getPromoEmpty");
	$.ajax({
		url: "../../getPromoEmpty",
		beforeSend: function (xhr) {
			$scope.cargandoPromosEmpty = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.promoEditando = resultado;
			$scope.cargandoPromosEmpty = false;
			$scope.$evalAsync();
		},
	});
};
$scope.rmPromoDefinitivo = function (fkPromo) {
	console.log("rmPromoDefinitivo");

	if (
		confirm("SEGURO DESEA ELIMINAR DEFINITIVAMENTE LA PROMO " + fkPromo + "??")
	) {
		$.ajax({
			url: "../../rmPromoDefinitivo",
			data: {
				fkPromo: fkPromo,
			},
			success: function (resultado, textStatus, jqXHR) {
				$scope.refrescar();
			},
		});
	}
};
