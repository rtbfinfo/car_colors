<script>

  import { fade } from "svelte/transition";
  
  let y
  
  </script>

<svelte:window bind:scrollY={y} />

{#if y > 50}

<div id="progress-bar"></div>
<nav class="fixed-nav-bar" in:fade>

      <a class="brand" href="https://www.rtbf.be/info?" rel="noreferrer" target="_blank">
        <img src="./rtbf.svg" alt="RTBF Logo" />
      </a>
      
      <div class="share">
      <!-- svelte-ignore a11y-missing-content -->
      <a href="https://www.facebook.com/sharer/sharer.php?u=https://www.rtbf.be/article/11267155" rel="noreferrer" target="_blank" alt="Facebook Logo"><img src="https://rtbfmedia.be/rtbfinfo/spotify_sound/pics/facebook_blanc_50_50.svg" alt="facebook Logo" class="svelte-11zqixe"></a>      <!-- svelte-ignore a11y-missing-content -->
      <a href="https://twitter.com/intent/tweet?text=https://www.rtbf.be/article/11267155" rel="noreferrer" target="_blank" alt="Twitter Logo"><img src="https://rtbfmedia.be/rtbfinfo/spotify_sound/pics/X_blanc_50_50.svg" alt="twitter(X) Logo" class="svelte-11zqixe"></a>      </div>

    </nav>

    {/if}

    

    <style>
.fixed-nav-bar {
    position: fixed;
    align-items: flex-end;
    justify-content: flex-end;
    top: 0;
    left: 0;
    z-index: 9998;
    width: 100%;
    height: 40px;
    background-color: #2e2e2e;
    box-shadow: 0 0 10px gray;
    opacity: .7;
    display: flex;
    line-height: 50px;
  }
  
  nav img {
    height: 30px;
    transform: translateY(15%);
  }
  
  nav .brand {
    flex: 1;
    align-self: flex-start;
    height: 40px;
    margin-left: 20px;
  }


.share{
    flex: -1;
    align-self: flex-end;
    height: 30px;
    margin-left: 20px;
    margin-right: 20px;
    transform: translateY(-30%);
  }

  /* Progress bar */
#progress-bar {
    --scrollAmount: 0%;
    background-color: #0057A2;
    width: var(--scrollAmount);
  
    /*  background: linear-gradient(to right, #F24E1E var(--scrollAmount), transparent 0);
    width: 100%; */
    
    height: 5px;
    position: fixed;
    top: 0;
    z-index:10000;
    margin-top: 35px;
  }

    </style>