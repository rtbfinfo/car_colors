<div class="image-grid">
    <div class="image-row">
        <div class="image image-01" />
        <div class="image image-02" />
    </div>
    <div class="caption">

        Une BMW 2002 Tii de 1973 et une Volkswagen Golf Gti de 1983, avec sa célèbre calandre rouge. - Crédit Dean Mouhtaropoulos/Getty Images & National Motor Museum/Heritage Images/Getty Images
    </div>
</div>

<style>
    * {
        border-width: 0;
    }

    .image-grid {
        padding: 5px;
    }

    .image-row {
        display: flex;
    }

    .image-row .image {
        margin: 15px 5px 15px 5px;
        height: 50vh;
    }

    .caption {
        text-align: right;
        font-size: 0.7em;
        margin-top: -10px;
        width: 100%;
        margin: 0 auto;
    }
    .image {
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center center;
    }

    .image-01 {
        background-image: url("../pics/BMW_orange.webp");
        flex: 1;
    }

    .image-02 {
        background-image: url("../pics/Golf_gti_black.webp");
        flex: 1;
    }

    @media screen and (max-width: 800px) {
        .image-row {
            flex-direction: column;
        }

        .image-row .image {
            flex-basis: auto;
        }
    }
</style>
