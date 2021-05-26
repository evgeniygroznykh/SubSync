import React, { useState, useEffect } from 'react'
import appConfig from './react-app-config'
import { Container } from 'react-bootstrap'
import ChannelListItem from "./ChannelListItem"
import MediaList from './MediaList'


export default function ChannelList() {
    const [error, setError] = useState(null)
    const [channels, setChannels] = useState([])
    const [selectedChannel, setSelectedChannel] = useState(channels[0])

    function selectChannel(event) {
        setSelectedChannel(event.target.id)
    }

    useEffect(() => {
        const apiBaseUrl = appConfig.api_base_url

        fetch(apiBaseUrl + '/get_channels')
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
            <Container>
                <Container style={{ width: "100vw", display: "flex", alignItems: "center", justifyContent: "center"}}>
                    <Container>
                        <ul id="channelList" className="centralized-content">
                            {
                                channels.map((channel, index) => {
                                        return (
                                            <ChannelListItem key={index} channel={channel} onclick_func={selectChannel} />
                                        )
                                    }
                                )
                            }
                        </ul>
                    </Container>
                </Container>
                <MediaList selected_channel={selectedChannel}/>
            </Container>
        )
    }
}
