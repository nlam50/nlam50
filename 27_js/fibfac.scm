
;factorial
(define fac (λ(n)
               (if (= n 1)
                   1
                   (* n (fac (- n 1))))))

(fac 1)
(fac 2)
(fac 3)
(fac 4)
(fac 5)

;fibonacci
(define fib (λ(n)
              (if (= n 0)
                  0
                  (if (= n 1)
                      1
                      (+ (fib(- n 1)) (fib(- n 2)))))))

(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
