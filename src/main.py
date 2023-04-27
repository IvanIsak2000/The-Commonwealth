from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
async def read_items():
	html_content = """
	<html>


<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=Oswald&family=Ruslan+Display&display=swap" rel="stylesheet">

<style type="text/css">

body{
background-image: url("static/logo1.png");
background-size:100%
}


a:link {
color: f6f8f7; /* Цвет ссылок */
font-size: 30px
}

a:visited {
    color: rgb(255, 255, 255); /* Цвет посещенных ссылок */
   }

a:active {
color:rgb(100, 197, 170) ; /* Цвет активной ссылки */
font-size: 35px
}

li { 
  position: relative; 
}

a {
  color: #fff;
  text-transform: uppercase;
  text-decoration: none;
  letter-spacing: 0.15em;
  display: inline-block;
  padding: 15px 20px;
  position: relative;
}

a::after { 
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  display: block;
  background: none repeat scroll 0 0 transparent;
  height: 2px;
  width: 0;
  background:rgb(100, 197, 170);
  transition: width 0.3s ease 0s, left 0.3s ease 0s;
}

a:hover::after { 
  width: 100%; 
  left: 0; 
}

div { float: left; /*Задаем обтекание*/
	line-height: 0px;/*Высота строки + верт. центрирования текста*/ 
	/* font-size:;  */
	left: 0px;
	top: 50px;
	margin-top: 10px; 
	width: 350px; /*Фиксируем ширину блока*/ 
	margin-right: 10px; text-align: center; /*Центрируем текст по горизонтали*/ }






.name{
font-family: 'Dela Gothic One', cursive;
font-family: 'Oswald', sans-serif;
color: rgb(100, 197, 170);
font-size: 250px;
padding: 10;
/* margin-left: 100px; */
position: relative;
top: 170px; 
left: 30px;


}



</style>
<head>
 	<title>The Commonwealth</title>

</head>

<body>
</div >
	<div id = 'line_block' ; class="link-ease-in-out">
		<center>
			
			<p class="a" ><a href="https://vk.com/thecommonwealth2020" style="text-decoration: none" title="">VKontakte</a></p>
		</center>
	</div>

	<div id = 'line_block' ;class="link-ease-in-out">
		<center>
			<p class="a" ><a href="https://vk.com/away.php?to=https%3A%2F%2Ft.me%2Fthecommonwealth2022" style="text-decoration: none" title="">Telegram</a></p>
		</center>
	</div>

	<div id = 'line_block' ; class="link-ease-in-out">
		<center>
			<p class="a" ><a href="https://vk.com/doc403210316_657773170?hash=wL0PIuCs5GU5CWq1g2cpODL01ziPSK0aZ8wXuO3jCmL&dl=Pas0Gzpci3aZ41tzhZUllpA1JWtojf3jLxAnbo5zCZg" style="text-decoration: none" title="">Charter</a></p>
		</center>
	</div>

	<div id = 'line_block' ; class="link-ease-in-out">
		<center>
			<p class="a" ><a href="https://vk.com/app5619682_-194667570" style="text-decoration: none" title="">Join</a></p>
		</center>
	</div>


	<div id = 'line_block' ; class="link-ease-in-out">
		<center>
			<p class="a" ><a href="https://vk.com/app5727453_-194667570?ref=group_menu" style="text-decoration: none" title="">Donate</a></p>
		</center>
	</div>


<p><span class="name" ><b>The Commonwealth</b></span></p>


 </body>
</html>

	"""
	return HTMLResponse(content=html_content, status_code=200)