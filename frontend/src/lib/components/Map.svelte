<script lang="ts">
    import {onMount} from 'svelte'
    import maplibregl from 'maplibre-gl';
    import 'maplibre-gl/dist/maplibre-gl.css'

    let mapContainer: HTMLDivElement | undefined = $state(undefined);
    let map: maplibregl.Map | undefined = undefined;;

    onMount(() => {
        if (!mapContainer) return;
        
        map = new maplibregl.Map({
            container: mapContainer, 
            style: 'https://tiles.openfreemap.org/styles/liberty',
            center: [90.3872, 23.7561],
            zoom: 12
        });

        map.addControl(new maplibregl.NavigationControl(), 'top-right');

        map.on('load', ()=> {
            if (!map) return

            map.addSource('transit-route-source', {
                type: 'geojson',
                data: { type: 'FeatureCollection', features: [] }
            })

            map.addLayer({
                id: 'transit-route-line',
                type: 'line',
                source: 'transit-route-source',
                layout: {
                    'line-join': 'round',
                    'line-cap': 'round'
                },
                paint: {
                    'line-color': ['get', 'color'], 
                    'line-width': 8,
                    'line-opacity': 0.8
                }
            });
        });

        return () => {
            map?.remove();
        }
    })

    async function handleFindRoute() {

        if (!map) {
            console.warn("Map is not initialized yet!");
            return;
        }

        try {
            const res = await fetch('http://127.0.0.1:8000/api/route/test');
            const geojsonData = await res.json();
            
            const source = map.getSource('transit-route-source') as maplibregl.GeoJSONSource;
            
            if (source) {
                source.setData(geojsonData);
            }
            
            map.flyTo({
                center: [90.3932, 23.7664], 
                zoom: 12.5,
                pitch: 40
            });
        } catch (error) {
            console.error("Failed to fetch route:", error);
        }
    }
</script>

<!-- <div bind:this={mapContainer} class="w-full h-screen"></div> -->

<div class="relative w-full h-screen">
    
    <div bind:this={mapContainer} class="w-full h-full"></div>

    <div class="absolute top-6 left-6 z-10 bg-white p-5 rounded-2xl shadow-xl border border-gray-100">
        <h1 class="text-2xl font-extrabold text-gray-800 mb-4 flex items-center gap-2">
            <span class="text-blue-600">Dhaka</span>Transit
        </h1>
        
        <button 
            onclick={handleFindRoute}
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-xl shadow-md transition-all"
        >
            MRT Line 6
        </button>
    </div>

</div>