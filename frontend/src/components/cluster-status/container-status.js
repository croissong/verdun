import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import ListItem from '@material-ui/core/ListItem';
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

const ContainerStatus = ({ title, subheader, icon, metrics }) => {
  const classes = useStyles();
  return (
    <ListItem style={{ flexWrap: 'wrap' }}>
      <Card style={{ width: '100%' }}>
        <div style={{ width: '100%', display: 'flex' }}>
          <CardHeader avatar={icon} title={title} subheader={subheader} />
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
          {metrics && (
            <Typography>
              Image: <code>{metrics.image}</code>
            </Typography>
          )}
        </CardContent>
      </Card>
    </ListItem>
  );
};
export default ContainerStatus;
