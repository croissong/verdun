import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import List from '@material-ui/core/List';
import HeartbeatIcon from '../../images/heartbeat.svg';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%'
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular
  }
}));

const Status = ({ loading, icon, title, children }) => {
  const classes = useStyles();
  return (
    <ExpansionPanel>
      <ExpansionPanelSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls="panel1a-content"
        id="panel1a-header"
      >
        {icon}
        {title && <h3>{title}</h3>}
        <div style={{ marginLeft: 'auto' }}>
          <HeartbeatIcon
            style={{ height: '2rem', width: '2rem', color: 'green' }}
          />
        </div>
      </ExpansionPanelSummary>
      <ExpansionPanelDetails>
        <List component="nav" style={{ width: '100%' }}>
          {children}
        </List>
      </ExpansionPanelDetails>
    </ExpansionPanel>
  );
};
export default Status;
