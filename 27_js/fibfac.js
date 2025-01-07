var fact = function(n) {
	if (n==1){
		return n;	
	}
	else return (n * fact(n-1));
}


var fib = function(n) {
	if (n == 0) {
		return 0;
		if (n == 1) {
			return 1;
		}
		else return ((fib(n -1)) + (fib(n -2)));
	}
	else return ((fib(n -1)) + (fib(n -2)));
}
