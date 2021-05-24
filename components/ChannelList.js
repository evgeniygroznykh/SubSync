import React, { useState, useEffect } from 'react'
import { Container } from 'react-bootstrap'
import ChannelListItem from "./ChannelListItem"

export default function ChannelList() {
    const [error, setError] = useState(null)
    const [channels, setChannels] = useState([])
    const [selectedChannel, setSelectedChannel] = useState("")

    function selectChannel(event) {
        setSelectedChannel(event.target.id)
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
        return (
            <div>
                {error.message}
            </div>
        )
    }
    else {
        return (
            <Container style={{ width: "100vw", display: "flex", alignItems: "center", justifyContent: "center"}}>
                <ul id="channelList" class="centralized-content">
                    {
                        channels.map((channel, index) => {
                                return (
                                    <ChannelListItem channel={channel} selected_channel_index={index} onclick_func={selectChannel} />
                                )
                            }
                        )
                    }
                </ul>
            </Container>
        )
    }
}
