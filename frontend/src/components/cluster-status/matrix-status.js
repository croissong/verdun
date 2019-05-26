import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import MatrixIcon from '../../images/matrix.svg';
import MatrixRiotIcon from '../../images/matrix-riot.svg';
import PostgresIcon from '../../images/postgres.svg';
import HeartbeatIcon from '../../images/heartbeat.svg';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%'
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular
  }
}));

const MatrixStatus = ({ loading, metrics }) => {
  const classes = useStyles();
  return (
    <ExpansionPanel>
      <ExpansionPanelSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls="panel1a-content"
        id="panel1a-header"
      >
        <MatrixIcon style={{ height: '2rem', width: '6rem' }} />
        <div style={{ marginLeft: 'auto' }}>
          <HeartbeatIcon
            style={{ height: '2rem', width: '2rem', color: 'green' }}
          />
        </div>
      </ExpansionPanelSummary>
      {metrics && (
        <ExpansionPanelDetails>
          <List component="nav" style={{ width: '100%' }}>
            <ListItem style={{ flexWrap: 'wrap' }}>
              <Card style={{ width: '100%' }}>
                <div style={{ width: '100%', display: 'flex' }}>
                  <CardHeader
                    avatar={
                      <MatrixIcon style={{ height: '2rem', width: '2rem' }} />
                    }
                    title="Synapse"
                    subheader="Matrix Homeserver"
                  />
                  <div
                    style={{
                      marginLeft: 'auto',
                      padding: '16px'
                    }}
                  >
                    <HeartbeatIcon
                      style={{
                        height: '2rem',
                        width: '2rem',
                        color: 'green'
                      }}
                    />
                  </div>
                </div>
                <CardContent>
                  <Typography>
                    Image: <code>{metrics['matrix-synapse'].image}</code>
                  </Typography>
                </CardContent>
              </Card>
            </ListItem>
            <ListItem style={{ flexWrap: 'wrap' }}>
              <Card style={{ width: '100%' }}>
                <div style={{ width: '100%', display: 'flex' }}>
                  <CardHeader
                    avatar={
                      <MatrixRiotIcon
                        style={{ height: '2rem', width: '2rem' }}
                      />
                    }
                    title="Riot"
                    subheader="Matrix Webclient"
                  />
                  <div
                    style={{
                      marginLeft: 'auto',
                      padding: '16px'
                    }}
                  >
                    <HeartbeatIcon
                      style={{
                        height: '2rem',
                        width: '2rem',
                        color: 'green'
                      }}
                    />
                  </div>
                </div>
                <CardContent>
                  <Typography>
                    Image: <code>{metrics['matrix-riot'].image}</code>
                  </Typography>
                </CardContent>
              </Card>
            </ListItem>
            <ListItem style={{ flexWrap: 'wrap' }}>
              <Card style={{ width: '100%' }}>
                <div style={{ width: '100%', display: 'flex' }}>
                  <CardHeader
                    avatar={
                      <PostgresIcon style={{ height: '2rem', width: '2rem' }} />
                    }
                    title="PostgreSQL Synapse "
                    subheader="Database for Synapse"
                  />
                  <div
                    style={{
                      marginLeft: 'auto',
                      padding: '16px'
                    }}
                  >
                    <HeartbeatIcon
                      style={{
                        height: '2rem',
                        width: '2rem',
                        color: 'green'
                      }}
                    />
                  </div>
                </div>
                <CardContent>
                  <Typography>
                    Image: <code>{metrics['postgres'].image}</code>
                  </Typography>
                </CardContent>
              </Card>
            </ListItem>
          </List>
        </ExpansionPanelDetails>
      )}
    </ExpansionPanel>
  );
};
export default MatrixStatus;
