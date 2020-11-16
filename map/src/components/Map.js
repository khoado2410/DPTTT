import React, { Component } from 'react';
import {MapContainer, Marker, Popup, TileLayer} from "react-leaflet";

//const AnyReactComponent = ({ text }) => <div>{text}</div>;

class SimpleMap extends Component {
    render() {
        return (
            // Important! Always set the container height explicitly
            <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={true} className='mapid'>
                <TileLayer
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <Marker position={[51.505, -0.09]}>
                    <Popup>
                        A pretty CSS3 popup. <br /> Easily customizable.
                    </Popup>
                </Marker>
            </MapContainer>
        );
    }
}

export default SimpleMap;