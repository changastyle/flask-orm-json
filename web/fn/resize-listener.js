$scope.ancho = 0;
$scope.anchoMinimo = 300;
$(document).ready(function () {
	$(window).trigger("resize");
	// 1 - TOOL TIPS:
	$('[data-toggle="tooltip"]').tooltip();

	$("#demoXL").carousel({
		interval: 6000,
		cycle: true,
	});
	$("#demoXS").carousel({
		interval: 6000,
		cycle: true,
	});
	// 2 - LISTENER DE SCROLL:
	//
	//
	// 3 - LISTENER DE RESIZE EVENT:
	$scope.xl = false;
	$scope.lg = false;
	$scope.md = false;
	$scope.sm = false;
	$scope.xs = true;

	$(".carousel").carousel({
		interval: false,
	});

	$(window).on("resize", function () {
		var win = $(this); //this = window
		$scope.ancho = win.innerWidth();

		if ($scope.ancho < $scope.anchoMinimoWEB) {
			console.log(
				"ANCHO MINIMO :" + $scope.anchoMinimoWEB + " | " + $scope.ancho
			);
		}

		if ($scope.ancho > 1200) {
			$scope.xl = true;
			$scope.lg = false;
			$scope.md = false;
			$scope.sm = false;
			$scope.xs = false;
			$scope.esteTamano = "xl";
		} else if ($scope.ancho < 1200 && $scope.ancho > 992) {
			$scope.xl = false;
			$scope.lg = true;
			$scope.md = false;
			$scope.sm = false;
			$scope.xs = false;
			$scope.esteTamano = "lg";
		} else if ($scope.ancho < 992 && $scope.ancho > 768) {
			$scope.xl = false;
			$scope.lg = false;
			$scope.md = true;
			$scope.sm = false;
			$scope.xs = false;
			$scope.esteTamano = "md";
		} else if ($scope.ancho < 768 && $scope.ancho > 576) {
			$scope.xl = false;
			$scope.lg = false;
			$scope.md = false;
			$scope.sm = true;
			$scope.xs = false;
			$scope.esteTamano = "sm";
		} else if ($scope.ancho < 576) {
			$scope.xl = false;
			$scope.lg = false;
			$scope.md = false;
			$scope.sm = false;
			$scope.xs = true;
			$scope.esteTamano = "xs";
		}

		if ($scope.xs || $scope.sm || $scope.md) {
			$scope.mostrarBusqueda = false;
		}

		$scope.$evalAsync();
		console.log(
			"RESIZE ancho:" +
				$scope.ancho +
				" | xs:" +
				$scope.xs +
				" | sm:" +
				$scope.sm +
				" | md: " +
				$scope.md +
				" | lg: " +
				$scope.lg +
				" | xl:" +
				$scope.xl
		);
	});

	$(window).trigger("resize");
});
