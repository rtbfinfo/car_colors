<script>
    import { createObserver } from "svelte-use-io";
  
    const { observer } = createObserver({
        rootMargin: "-50%",
    });
    let video;
    const play = () => {
        video.play();
    };
    const pause = () => {
        video.pause();
    };
  </script>
  
  <div class="report">
    <video
    playsinline
preload=“metadata”
    src="./vids/all_kia.mp4"
    muted
    loop
    bind:this={video}
    use:observer
    on:intersecting={play}
    on:unintersecting={pause}
    />
    
  </div>
  <p style="text-align:right; font-size: 0.8em;line-height:1.2em">Les 9 couleurs disponibles pour la Kia Stonic (l'animation tourne en boucle, vous pouvez passer à la suite).</p>
  <style>
    .report {
        margin: 0 auto;
        justify-content: center;
        width: 100%;
        display: flex;
    }
    video {
        width: 100%;
        outline: 4px solid white;
outline-offset: -4px;
    }

    @media screen and (max-width: 550px) {
        video {
            width: 100vw;
            height: auto;
	}
}
  </style>
  