import React, { useState, useEffect } from 'react'
import { Container } from 'react-bootstrap'
import videoimg from './img/video.jpg'
import subtitleimg from './img/subtitle.jpg'
import loading from './img/loading_animation.gif'
 

export default function MediaList (props) {
    const selected_channel = props.selected_channel ? props.selected_channel : ""
    const [isChannelSelected, setIsChannelSelected] = useState(false)

    useEffect(() => {
        if (selected_channel) {
            setIsChannelSelected(true)
        }
    }, [selected_channel])

    if (document.getElementById("channelList") != null) {
        if (document.getElementById("channelList").hasChildNodes && !isChannelSelected) {
            return (
                <Container className="selection-text-message centralized-content">Select channel from channel list</Container>
            )
        }
        else {
            return (
                <div id="media-content">
                    <div id='clip-list-container'>
                        <table id="clip-list">
                            <thead>
                                <tr>
                                    <th className="media-list-header">Clips:</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    props.selected_channel.channelClips.map((clip, index) => {
                                        return (
                                            <div>
                                                <tr key={index}>
                                                    <td>
                                                        <span style={{ display: "inline-block", width: "150px" }}>
                                                            <img className="icon" src={videoimg} alt=""></img>
                                                                {clip.clip_name}
                                                        </span>
                                                        <span>
                                                            <input type="checkbox" checked={clip.has_sub_on_m}></input>
                                                            <input type="checkbox" checked={clip.has_sub_on_b}></input>
                                                        </span>
                                                    </td>
                                                </tr>
                                            </div>
                                            )
                                        }
                                    )
                                }
                            </tbody>
                        </table>
                    </div>
                    <div id='subtitle-list-container'>
                    <table id="subtitle-list">
                        <thead>
                            <tr>
                                <th className="media-list-header">Subtitles:</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                props.selected_channel.channelSubtitles.map((subtitle, index) => {
                                    return (
                                        <div>
                                            <tr key={index}>
                                                <td><span><img className="icon" src={subtitleimg} alt=""></img>{subtitle.sub_name}</span></td>
                                            </tr>
                                        </div>
                                        )
                                    }
                                )
                            }
                        </tbody>
                        </table>
                    </div>
                </div>        
            )
        }
    }
    else {
        return (
            <Container style={{ width: "100vw", display: "flex", alignItems: "center", justifyContent: "center", marginTop: "10%"}}>
                <Container>
                    <img alt="" src={loading}></img>
                </Container>
                <Container style={{ marginLeft: "75px", fontFamily: "Courier New, monospace" }}>
                    Your subtitles are on the way..
                </Container>
            </Container>
        )
    }
}