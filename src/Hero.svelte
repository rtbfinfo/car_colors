<script>



</script>


<div class="hero">
  <h2><a href='https://www.rtbf.be/archive/decrypte' target='_blank' style="color:white;font-weight:700;text-decoration:none;" rel=noreferrer>Décrypte</a></h2>
  <div class="container">
  </div>
  <div class="text">
    <h3>EN 50 ANS</h3>
    <h1 class="title">
      <span>Comment et pourquoi nos voitures ont perdu</span>
      <span><mark>LEURS COULEURS</mark></span>
  </h1>
   <p>Par Ambroise Carton</p>
</div>
<div class="mouse_wheel">
  <div class="anim-scroll">
  <div class="anim-scroll--wheel"></div>
</div>
</div>
<div class="image-credit">© carsized.com</div>

</div>



<style>

*{
  /*outline: 1px solid red;*/
  color: white !important;
}

.title span {
            display: block;
        }

        mark {
          background-image: linear-gradient(to right, #F27121, #808080);
  border-radius: 6px;
  padding: 3px 6px;
  font-size: 2em;
  line-height: 2;

}
.hero {
    display: flex;
    flex-direction: column;
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                      url("../pics/hero.png");
    height: 100vh;
    width: 100%;
    margin: 0 auto;
    background-repeat: no-repeat;
    background-size: cover;

    background-position: center center;
    align-items: center;
    justify-content: center;
    z-index: 1;
}
      
.text {
    font-size: 1.4rem;
    text-align: center;
    color: white 
}

 h1 {
      font-size: 2em;
      font-weight: 700;
      margin-bottom: 15px;
      text-align: center;
    }
     h2{
      font-size: 0.8em;
      font-weight: 300;
      text-align: center;
      max-width: 80%;
      margin: 0 auto;
      margin-top: 70px;
    }

    h3{
      font-size: 1.7em;
    }

    p {
    font-size: 0.7em;
  }

.mouse_wheel {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 1;
  position: absolute;
    bottom: 20px;
}
.anim-scroll {
  border: 2px solid #fff;
  border-radius: 22px;
  height: 40px;
  position: relative;
  width: 20px;
  z-index: 1;
}
.anim-scroll--wheel {
  animation: scroll 2.5s ease infinite;
  background: #fff;
  border-radius: 30px;
  height: 8px;
  left: calc(50% - 1.5px);
  position: absolute;
  right: 50%;
  top: 8px;
  width: 3px;
}
@keyframes scroll {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(16px);
  }
  51% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateY(0);
  }
}

.image-credit {
color: #fff;
display: inline-block;
font-size: 11px;
font-weight: 300;
padding: 5px 8px;
position: absolute;
bottom: 0;
right: 0;
z-index: 9999;
}



  @media screen and (max-width: 550px) {

  h1 {
      font-size: 0.6em;

    }
     h2{
      font-size: 0.8em;
      max-width: 90%;
    }


  }

</style>