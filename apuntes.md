
## Comandos usados en la demo

#### iniciar scrapy:

```console
scrapy shell
```

#### descargar un sitio web:

```console
fetch("https://www.reddit.com/r/dankmemes/")
```


#### abrir el html en local via browser:

```console
view(response)
```


#### texto de la respuesta:

```console
print response.text
```


#### Buscamos: título del post, fecha y votos.

Abrir el navegador, inspeccionar y buscar las etiquetas concretas.

#### Extraer títulos:

```console
response.css(".title::text").extract()
```


#### título es la TAG html, text es lo que queremos extraer.

con 

```console
response.css(".title::text").extract_first()
```
 

#### nos quedamos con el primero

con 

```console
response.css(".title").extract()
```
 seleccionamos toda la tag

#### votos:

concatenando dos clases class="score unvoted"

```console
response.css(".score.unvoted").extract_first()
```


#### contabilizar votos:

```console
response.css(".score.unvoted::text").extract()
```


#### fecha el post:

en reddit si buscamos time, nos puede dar algo tipo "post publicado hace X horas", queremos la fecha

```console
foo@bar:~$ whoami
foo
```
con time::attr(title) nos queamos con el contenido de title="ESTO" DENTRO de la etiqueta time

```console
response.css("time::attr(title)").extract()
```


#### Empezar un proyecto:

```console
scrapy startproject dankmemes
```



settings.py contiene la configuración del proyecto

spiders contiene los "bots"

#### generamos una araña con:

```console
scrapy genspider dankbot www.reddit.com/r/dankmemes/
```


name: nombre con el que haremos referencia al bicho

allowed_domains: dominios en los que el bicho puede trabajar

parse(self.response): Esto es importante, aquí definiremos el procesado de datos

#### extraer url del post a partir del título

```console
url = response.css('.title.may-blank::attr(href)').extract(
```
)


#### extraer imagen "meme" del post

```console
response.css('img.preview::attr(src)').extract()
```



#### log en csv de todo lo que scrapeamos

#Export as CSV Feed
FEED_FORMAT = "csv"
FEED_URI = "dankmemes.csv"

lo vemos en:

```console
cat dankmemes.csv 
```
#### capturar archivos

```console
pip install wget
```

```console
filename = wget.download(img, out="/home/sandbox/memes/")
```




