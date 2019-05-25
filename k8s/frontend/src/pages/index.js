import React from 'react';
import Layout from '../components/layout';
import SEO from '../components/seo';
import ClusterStatus from '../components/cluster-status';

const ClientFetchingExample = () => (
  <Layout>
    <SEO title="Status" />
    <ClusterStatus />
  </Layout>
);
export default ClientFetchingExample;
