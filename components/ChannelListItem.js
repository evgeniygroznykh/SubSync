import React from 'react'
import tntlogo from './img/tntlogo.png'
import tnt4logo from './img/tnt4logo.jpg'
import _2x2logo from './img/_2x2logo.jpg'

export default function ChannelListItem (props) {
    switch (props.channel.channelName) {
        case "tnt": return (       
                <li key={props.selected_channel_index}>
                    <img src={tntlogo} id={props.channel.channelName} onClick={props.onclick_func}></img>
                </li>
            )
        case "tnt4": return (    
                <li key={props.selected_channel_index}>
                    <img src={tnt4logo} id={props.channel.channelName} onClick={props.onclick_func}></img>
                </li>
            )
        case "2x2": return (           
                <li key={props.selected_channel_index}>
                    <img src={_2x2logo} id={props.channel.channelName} onClick={props.onclick_func}></img>
                </li> 
            )
    }
}