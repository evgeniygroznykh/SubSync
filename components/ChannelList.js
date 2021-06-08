import React, { useState, useEffect } from 'react'
import appConfig from './react-app-config'
import { Container } from 'react-bootstrap'
import ChannelListItem from "./ChannelListItem"
import MediaList from './MediaList'


export default function ChannelList() {
    const [error, setError] = useState(null)
    const [channels, setChannels] = useState([])
    const [selectedChannelName, setSelectedChannelName] = useState(null)
    const apiBaseUrl = appConfig.api_base_url
    const apiPollPeriod = appConfig.api_poll_period_ms
    const endpoint = '/get_channels'

    function selectChannel(event) {
        setSelectedChannelName(event.target.id)
        pollApi()
    }

    function pollApi() {
        fetch(apiBaseUrl + endpoint)
        .then(res => res.json())
        .then(
            (result) => {
                setChannels(result)
                setError(null)
            },
            (error) => {
                setChannels([])
                setError(error)
            }
        )
    }

    useEffect(() => {
        const id = setInterval(
            () => pollApi()
        , apiPollPeriod);
      
        return () => clearInterval(id);  
      }, []);

    if (error || channels === []) {
        return (
            <Container style={{ width: "100vw", display: "flex", alignItems: "center", justifyContent: "center", marginTop: "10%"}}>API is down: {error.message}</Container>
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
                <MediaList selected_channel={channels.filter(channel => channel.channelName === selectedChannelName)[0]}/>
            </Container>
        )
    }
}
