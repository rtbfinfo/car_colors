<script>
	import Scroll from "./Scrolly.svelte";
  
	let currentStep;
  
	let slide = "0";
  
	const steps = ["<p>Prenons les températures moyennes en juillet à Villar-Saint-Pancrace, la station météo la plus proche du sommet du Galibier. Il y a des années plus chaudes, d’autres moins chaudes. Rien de bien inquiétant à première vue.</p>", 
	"<p>Faisons maintenant des «&nbsp;warming stripes&nbsp;» (ou «&nbsp;climate stripes&nbsp;», littéralement des «&nbsp;barres du réchauffement&nbsp;»). L'idée de ce type de graphe revient <a href='https://showyourstripes.info/' target='_blank' rel=noreferrer>au climatologue Ed Hawkins</a>, de l'université de Reading en Angleterre. Le principe est simple&nbsp;: on prend une période de référence de 30 ans, ici 1971-2000, et on fait une moyenne des températures sur ces trois décennies. On compare ensuite la température moyenne de chaque année à la température de la période de référence. </p", 
	"<p>Plus c'est bleu, plus l'année a été froide par rapport à la période de référence. Et à l'inverse, plus c'est rouge, plus on est au-dessus. Vous le voyez, le réchauffement, maintenant&nbsp;? La dernière fois que la température moyenne a été plus basse que la normale, c’était <mark style='background-color: #C9E1ED; padding: 0 5px 0 5px; border-radius: 5px;'><strong>en 2014</strong></mark>  qui fut, vous vous en rappelez peut-être, un «&nbsp;été pourri&nbsp;».</p>",
	"<p>Côté chaleur, les étés  <mark style='background-color: #E37F65; padding: 0 5px 0 5px; border-radius: 5px;'><strong>2003</strong></mark>, <mark style='background-color: #CB4B44; padding: 0 5px 0 5px; border-radius: 5px;'><strong>2006</strong></mark>, <mark style='background-color: #67001F; color: white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>2015</strong></mark> et <mark style='background-color: #67001F; color: white; padding: 0 5px 0 5px; border-radius: 5px;'><strong>2022</strong></mark> sont eux en rouge de plus en plus foncé. Ils sont donc bien au-dessus de la moyenne climatique de 1971-2000.</p>",
];
  
	$: if (currentStep == 0) {
		  slide="0";
  
	} else if (currentStep == 1) {
	  slide="1";  }
	  else if (currentStep == 2) {
	  slide="2";  }
	  else if (currentStep == 3) {
	  slide="3";  }
	  else if (currentStep == 4) {
	  slide="4";  }
	  else if (currentStep == 5) {
	  slide="5";  }
	  else if (currentStep == 6) {
	  slide="6";  }


  
  </script>

<div class="section-container">

	<div class="steps-container">

		<Scroll bind:value={currentStep}>
			{#each steps as text, i}
			  <div class="step" class:active={currentStep === i}>

				<div class="step-content">
				  {@html text}
				</div>
			  </div>
			{/each}
			<div class="spacer"/>
		  </Scroll>
		  
    </div>
	
	<div class="sticky">
		<iframe src='https://flo.uri.sh/story/1962904/embed#slide-{slide}' title='Interactive or visual content' class='flourish-embed' frameborder='0' scrolling='no' style='width:100%;height:90vh;'></iframe>
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
    top: 7%;
		flex: 1 1 60%;
    width: 60%;
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
      width: 95%;
			margin: auto;
    }
	.steps-container{
		margin-top: -80vh
	}
  }



  </style>
