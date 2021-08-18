import React, { Component } from 'react';
import './App.css';

import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.webpack.css'; // Re-uses images from ~leaflet package
import 'leaflet-defaulticon-compatibility';
class App extends Component{


  render() {
    const county_line = [

        [28.347246, -81.657513],
        [28.766739, -81.658090],
        [28.767086, -81.646700],
        [28.785487, -81.645467],
        [28.784826, -81.415248],
        [28.754995, -81.417294],
        [28.717192, -81.438755],
        [28.713630, -81.458951],
        [28.640360, -81.459778],
        [28.639226, -81.328007],
        [28.610582, -81.328033],
        [28.613099, -80.988455],
        [28.591803, -80.943633],
        [28.541769, -80.939222],
        [28.510202, -80.888150],
        [28.471259, -80.873936],
        [28.433525, -80.899962],
        [28.348407, -80.874180],
        [28.347198, -81.657300],
    ]

    const lines_fill = { fillColor: 'blue'}

    return(
      <MapContainer className ="map" center={[28.301962, -81.200638]} zoom={11} scrollWheelZoom={true}>
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Polyline pathOptions={lines_fill} positions={county_line} />

        <Marker position={[28.450120539082775, -81.47450039368225]} >
          <Popup>
            A pretty CSS3 popup. <br /> Easily customizable.
          </Popup>
        </Marker>

      </MapContainer>
    );
  }
}

export default App;
