/** @jsx jsx */

import React from 'react';
import { jsx } from '@emotion/core';
import { useTranslation } from 'i18n';

import List from 'antd/lib/list';
import { StatGroup, StatsFromCustomSet } from 'common/types';
import { customSet } from 'graphql/fragments/__generated__/customSet';

interface IStatTable {
  group: StatGroup;
  statsFromCustomSet: StatsFromCustomSet | null;
  customSet?: customSet | null;
}

const StatTable: React.FC<IStatTable> = ({
  group,
  statsFromCustomSet,
  customSet,
}) => {
  const { t } = useTranslation('stat');
  return (
    <List
      css={{ background: 'white' }}
      itemLayout="horizontal"
      size="small"
      bordered
      dataSource={group}
      rowKey={item => item.stat}
      renderItem={item => (
        <List.Item
          css={{
            display: 'flex',
            justifyContent: 'space-between',
          }}
        >
          <div css={{ fontSize: '0.75rem' }}>{t(item.stat)}</div>
          <div css={{ fontSize: '0.75rem' }}>
            {(statsFromCustomSet &&
              customSet &&
              (item.customCalculateValue
                ? item.customCalculateValue(statsFromCustomSet, customSet)
                : statsFromCustomSet[item.stat])) ||
              0}
          </div>
        </List.Item>
      )}
    />
  );
};

export default StatTable;
