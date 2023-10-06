<script>
	import Scroll from "./Scrolly.svelte";


  
    let currentStep;
    let slide = "0";
    let contentLink;
	let iframeHeight="90vh";

  
	const steps = [
		{ text:"<p>Nous avons photographié les voitures depuis les hauteurs de la E411 un lundi d’automne. Une photo par seconde pendant quarante minutes, soit le temps nécessaire pour voir passer 1000 voitures. <strong>Scrollez vers le bas pour voir le résultat<strong>.</p>", stepNumber: 1 },
		{ text:"<p>À l’aide d’un script informatique, nous avons automatiquement isolé les véhicules sur chaque photo.</p>", stepNumber: 2 },
		{ text:"<p>Puis nous avons extrait la couleur de chaque carrosserie. Voici un petit échantillon. Coucou la voiture jaune&nbsp;!</p>", stepNumber: 3 },
		{ text:"<p>Pour enfin réaliser cette mosaïque qui reprend la couleur dominante pour 1000 carrosseries.</p>", stepNumber: 4 },
		{ text:"<p>Mettons un peu d'ordre dans tout ça, du plus clair au plus foncé... Un constat s'impose : les couleurs dites «&nbsp;originales&nbsp;» sont clairement minoritaires dans notre jeu de données.</p>", stepNumber: 5 },
		{ text:"<p>En quarante minutes, une seule voiture <mark style='background-color: #f5cd6e; padding: 0 5px 0 5px; border-radius: 5px;'><strong>jaune</strong></mark> s'est donc présentée. À part les <mark style='background-color: #de0427; color:white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>rouges</strong></mark> et les <mark style='background-color: #91b0de; padding: 0 5px 0 5px; border-radius: 5px;'><strong>bleues</strong></mark>, seule un <mark style='background-color: #9cb888; padding: 0 5px 0 5px; border-radius: 5px;'><strong>vert olive</strong></mark> et un <mark style='background-color: #6Dcdff; padding: 0 5px 0 5px; border-radius: 5px;'><strong>bleu ciel</strong></mark> sortent du lot. Notez que ce qui peut apparaître comme du bleu ciel est sans doute du gris, c'est dû aux reflets du soleil sur la carrosserie.</p>", stepNumber: 6 },
		{ text:"<p>Cela ne fait que confirmer une tendance mise en évidence par Axalta, l'un des principaux producteurs mondiaux de peintures pour voitures qui observe les couleurs tendance en Europe depuis les années 80. Il y a 40 ans, le <mark style='background-color: #de0427; color:white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>rouge</strong></mark>, le <mark style='background-color: #06a082; padding: 0 5px 0 5px; border-radius: 5px;'><strong>vert</strong></mark> et même le <mark style='background-color: #f5cd6e; padding: 0 5px 0 5px; border-radius: 5px;'><strong>jaune</strong></mark> trouvaient encore leur place dans le top 5.</p>", stepNumber: 7 },
		{ text:"<p>Bon dernier au milieu des années 90, le <mark style='background-color: #D1D3D4; color:white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>gris</strong></mark> prend la tête au début des années 2000.</p>", stepNumber: 8 },
		{ text:"<p>À l’aube des années 2010, la tendance est installée : cinquante nuances de <mark style='background-color: #D1D3D4; color:white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>gris</strong></mark> avec quelques touches de <mark style='background-color: black; color:white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>noir</strong></mark> et de <mark style='background-color: #0082DC; color:white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>bleu</strong></mark> ici et là.</p>", stepNumber: 9 },
];
  
    $: {
        if (currentStep === 0) {
            slide = "video";
            contentLink = "./vids/timelapse_desktop.mp4";
        } else if (currentStep === 1) {
            slide = "image";
            contentLink = "./pics/all_cars_desktop.webp";
        } else if (currentStep === 2) {
            slide = "image";
            contentLink = "./pics/car_example.webp"
        } else if (currentStep >= 3 && currentStep <= 5) {
        slide = "flourish";
        contentLink = `https://flo.uri.sh/story/2049120/embed#slide-${currentStep - 3}`;
		iframeHeight = "100vh";
    }
	else if (currentStep >= 6 && currentStep <= 8) {
        slide = "flourish";
        contentLink = `https://flo.uri.sh/story/2049127/embed#slide-${currentStep - 6}`;
		iframeHeight = "70vh";
    }
    }
  
  </script>

<div class="section-container">

	<div class="steps-container">

		<Scroll bind:value={currentStep}>
			{#each steps as step, i}
				<div class="step" class:active={currentStep === i}>
					<div class="step-content">
						{@html step.text} <span style="text-align: right; color: grey;font-weight: 900;font-size: 0.8em">{step.stepNumber}/9</span>
					</div>
				</div>
			{/each}
			<div class="spacer"/>
		</Scroll>
		
		  
    </div>

	<div class="sticky">
        {#if slide === "video"}
            <video key="video" class='picture' autoplay muted loop playsinline preload=“metadata”>
                <source src={contentLink} type="video/mp4">
            </video>
			
        {:else if slide === "image"}
            <img key="image-{currentStep}" class='picture' src={contentLink} alt="" />

		{:else if slide === "flourish"}
        <iframe key="iframe-{currentStep}" src={contentLink} title='Interactive or visual content' class='flourish-embed' frameborder='0' scrolling='no' style='width:100%;height:{iframeHeight};'></iframe>
    {/if}
    </div>
</div>
	
  

  
  
  
  <style>
	

	/* The fixed chart */
  
	.flourish-embed {
		width: 100vw;
	  height: 100vh;
	  position: sticky;
	  top: 0;
	  margin: auto;
	  margin-top: 70px;
	}
	
	.picture {
		width:100vw;
height: auto;
	  position: sticky;
	  top: 0;
	  margin: auto;
	  position: absolute;
		left: 0;
	}

	.flourish-embed, .picture {
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
	will-change: transform;
}

	/* Scrollytelling CSS */
	.step {
	  height: 80vh;
	  display: flex;
	  place-items: center;
	  justify-content: center;
	  z-index: 100;
	}

    .sticky {
    position: sticky;
    top: 0;
	flex: 1 1 100%;
    width: 100%;
	z-index: 9;
	height: 100vh;
  }

  .spacer {
    height: 20vh;
  }

  .section-container {
    margin-top: 1em;
    text-align: center;
    transition: background 100ms;
    display: flex;
	flex-direction: column-reverse;

  }

  .step-content {
	background-color: rgba(245, 245, 245, 0.8);
			color: black;
			border-radius: 10px;
			padding: 0.5rem 1rem;
			display: flex;
			flex-direction: column;
			justify-content: center;
			transition: background 500ms ease;
			box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
			z-index: 10;
			font-size: 1rem;
		  text-align: left;
			  width: 75%;
			  margin: auto;
			  max-width: 500px;
  }

	
	
  .steps-container,
  .sticky {
    height: 100%;
  }

  .steps-container {
    flex: 1 1 40%;
    z-index: 10;
  }
	
  @media screen and (max-width: 768px) {
    .section-container {
      flex-direction: column-reverse;
    }
    .sticky {
      width: 100%;
			margin: auto;
    }

	.picture {
	  margin-top: 50%;
	}
  }



  </style>
