import React from 'react'
import { Container } from 'react-bootstrap'
import tntlogo from './img/tntlogo.jpg'
import tnt4logo from './img/tnt4logo.jpg'
import _2x2logo from './img/_2x2logo.jpg'
import mplogo from './img/mplogo.jpg'
import tv3logo from './img/tv3logo.jpg'
import fridaylogo from './img/fridaylogo.jpg'


export default function ChannelListItem (props) {
    const img_container_style = {
        width: "100px",
        height: "80px",
        display: "flex", 
        alignItems: "center", 
        justifyContent: "center",
        border: "1.5px ridge",
        margin: "5px"
    }

    const imageUrls = {
        "TNT": tntlogo,
        "TNT4" : tnt4logo,
        "2x2" : _2x2logo,
        "Match Premiere" : mplogo,
        "TV3" : tv3logo,
        "Friday" : fridaylogo
    }

    return (    
        <Container style={ img_container_style }>   
            <li className="centralized-content">
                <img src={imageUrls[props.channel.channelName]} id={props.channel.channelName} onClick={props.onclick_func} style={{ cursor: "pointer" }} alt=""></img>
            </li>
        </Container>
    )
}