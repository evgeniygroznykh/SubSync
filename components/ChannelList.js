import React, { useState, useEffect } from 'react'
import { Container } from 'react-bootstrap'


export default function ChannelList() {
    const [error, setError] = useState(null)
    const [channels, setChannels] = useState([])
    const [selectedChannel, setSelectedChannel] = useState(channels ? channels[0] : null)

    function selectChannel(event) {
        setSelectedChannel(event.target.innerText)
    }

    useEffect(() => {
        fetch('http://127.0.0.1:8001/get_channels')
        .then(res => res.json())
        .then(
            (result) => {
                setChannels(result)
            },
            (error) => {
                setError(error)
            }
        )
    }, [])

    if (error) {
        return(
            <div>
                {error.message}
            </div>
        )
    }
    else {
        return(
            <Container className="d-flex justify-content-center align-items-center" style={{minHeight: "100vh"}}>
                <ul id="channelList">
                    {channels.map((channel, index) => (
                        <li key={index} onClick={selectChannel}>{channel}</li>
                    ))}
                </ul>
            </Container>
        )
    }
}
