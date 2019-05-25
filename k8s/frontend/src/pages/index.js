import React, { Component } from 'react';
import axios from 'axios';
import parsePrometheusTextFormat from 'parse-prometheus-text-format';
import { merge } from 'lodash';
import Layout from '../components/layout';
import SEO from '../components/seo';

class ClientFetchingExample extends Component {
  state = { loading: false, error: false, metrics: null };

  componentDidMount() {
    this.fetchMetrics();
  }

  render() {
    if (this.state.metrics) {
      const metrics = this.state.metrics;
      const matrix = metrics['comm-tools']['matrix-synapse'];
      return (
        <Layout>
          <SEO title="Home" />
          Matrix: ready = {matrix.ready} image = {matrix.image}
        </Layout>
      );
    }
    return (
      <Layout>
        <SEO title="Home" />
        nodata
      </Layout>
    );
  }

  fetchMetrics = () => {
    this.setState({ loading: true });
    axios
      .get('/metrics')
      .then(({ data }) => {
        let metrics = parsePrometheusTextFormat(data);
        metrics = normalizeMetrics(metrics);
        this.setState({
          loading: false,
          metrics
        });
      })
      .catch(error => {
        this.setState({ loading: false, error });
      });
  };
}
export default ClientFetchingExample;

const metricMappers = {
  kube_pod_container_status_ready: ({ value }) => ({ ready: value }),
  kube_pod_container_info: ({ labels: { image } }) => ({ image })
};

const normalizeMetrics = data =>
  data.reduce((res, { name, metrics }) => {
    const mapper = metricMappers[name];
    if (!mapper) {
      return res;
    }

    const normalized = metrics.reduce((res, metric) => {
      const {
        labels: { namespace, container }
      } = metric;
      return merge(res, {
        [namespace]: {
          [container]: mapper(metric)
        }
      });
    }, res);

    return merge(res, normalized);
  }, {});
