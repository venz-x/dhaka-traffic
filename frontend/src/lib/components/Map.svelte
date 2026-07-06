<script lang="ts">
    import {onMount} from 'svelte'
    import maplibregl from 'maplibre-gl';
    import 'maplibre-gl/dist/maplibre-gl.css'

    let mapContainer: HTMLDivElement | undefined = $state(undefined);

    onMount(() => {
        if (!mapContainer) return;
        
        const map = new maplibregl.Map({
            container: mapContainer, 
            style: 'https://tiles.openfreemap.org/styles/liberty',
            center: [90.3872, 23.7561],
            zoom: 12
        });

        map.addControl(new maplibregl.NavigationControl(), 'top-right');

        map.on('load', ()=> {
            
        })

        return () => {
            map.remove();
        }
    })
</script>

<div bind:this={mapContainer} class="w-full h-screen"></div>