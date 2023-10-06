<div class="wrapper">
  <div class="container">
    <p><a href='https://www.rtbf.be/archive/decrypte' target='_blank' style="color:white !important;font-weight:700;text-decoration:none;" rel=noreferrer>Décrypte</a></p>
    <p>En 50 ans</p>
    <h2><big>COMMENT</big> et <big>POURQUOI</big><br>nos voitures ont perdu</h2>
    <h1>des couleurs</h1>


    <p style="text-align: center">🚗 🚕 🚗 🚕 🚗 🚕 🚗</p>

    <p>Par Ambroise Carton</p>

    <p style="text-align: center">🚗 🚕 🚗 🚕 🚗 🚕 🚗</p>

  </div>

  <div class="mouse_wheel">
    <div class="anim-scroll">
    <div class="anim-scroll--wheel"></div>
  </div>
</div>
</div>

<style>


* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


:root {
  --color-1: #186cb8;
  --color-2: #2a9a9f;
  --color-3: #f1b211;
  --color-4: #e83611;
  --color-5: #f9002f;
}


.wrapper {
  background: #2E2E2E;
  line-height: 1;
  min-height: 100%;
  display: grid;
  place-items: center;
  height: 100vh;
}

h1 {
  font-family: "Exo", sans-serif;
  font-size: 15vw;
  font-weight: 900;
  margin: auto;
  text-transform: uppercase;
  background: linear-gradient(219deg, 
    var(--color-1) 19%, 
    transparent 19%,transparent 20%, 
    var(--color-2) 20%, var(--color-2)  39%,
    transparent 39%,transparent 40%, 
    var(--color-3) 40%,var(--color-3) 59% ,
    transparent 59%,transparent 60%, 
    var(--color-4) 60%, var(--color-4) 79%,
    transparent 79%, transparent 80%, 
    var(--color-5) 80%);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
}

h2{
  font-size: 2vw;
  color: white;
  margin: 0 auto;
  text-align: center;
}

p{
  color: white;
}

p, h2 {
    margin: 20px 0; /* Adjust this value as needed */
}

.container {
  margin-left: auto;
    margin-right: auto;
    overflow: hidden !important;
  text-align: center;
  background: radial-gradient(circle at 1.4% 1.4% ,var(--color-1) .8%,transparent  .8% ), 
    radial-gradient(circle at 5.5% 3%,var(--color-2) .45% ,transparent .45% ), 
    radial-gradient(circle at 2.5% 3.5%,var(--color-3) .5% ,transparent .5% ), 
    radial-gradient(circle at 4.5% 1.2%,var(--color-4) .25%,transparent .25% ),

}


.mouse_wheel {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 1;
  position: absolute;
    bottom: 7%;
    left: 50%; 
  transform: translateX(-50%); 
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


@media screen and (min-width: 768px) {
  h1 {
    font-size: 6.5rem;
  }
}

@media screen and (max-width: 768px) {
  h2 {
    font-size: 20px;

  }
}


</style>