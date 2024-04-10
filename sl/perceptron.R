perceptron <- function(X, y, random_seed = 553){

  X <- cbind(1, X)
  set.seed(random_seed)
  w <- c(runif(n = 3, min = 0, max = 1))
  clasificaciones <- predict_clase(X = X, w = w)
  errores_clasificacion <- which((clasificaciones != y) == FALSE)
  
    while (length(errores_clasificacion) > 0){
    i <- sample(x = errores_clasificacion, size = 1)
    w <- w + X[i,] * y[i]
    clasificaciones <- predict_clase(X= X, w = w)
    errores_clasificacion <- which((clasificaciones == y) == FALSE)
  }
  return(w)
}

predict_clase <- function(X, w){
  clase_predicha <- apply(X = X, MARGIN = 1, FUN = function(x){crossprod(x, w)})
  clase_predicha <- sign(clase_predicha)
  return(clase_predicha)
}

X <- matrix(c(8, 4, 9, 7, 9, 4, 10, 2, 8, 7, 4, 4,1, 2, 7, 10, 7,
              10, 6, 8, 10, 7, 3, 5, 4, 6, 3, 5), ncol=2, byrow = FALSE)
y <- c(1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1)

hiperplano <- perceptron(X = X, y = y)
hiperplano

library(ggplot2)
datos <- data.frame(X, y)
ggplot(data = datos, aes(x= X1, y = X2, color = as.factor(y))) +
  geom_point() +
  geom_abline(intercept = -(hiperplano[1]/hiperplano[3]),
              slope = -(hiperplano[2] / hiperplano[3]),linewidth = 1)  +
  theme_bw() +
  theme(legend.position = "none")
