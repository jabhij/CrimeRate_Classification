import plotly.express as px

class MapScatter:
    def __init__(self, df):
        self.df = df
        self.clat = 37.773972
        self.clon = -122.431297
    
    # yearly
    def map_crimes(self, police_dept=None):
        df = self.df.sort_values(by='time')

        if police_dept:
            df = df[self.df['police_dept'] == police_dept]

        fig = px.scatter_mapbox(
            data_frame=df,
            lat='latitude',
            lon='longitude',
            color='category',
            hover_name='address',
            mapbox_style='carto-positron',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='year',
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # monthly
    def map_crimes_by_year(self, year, police_dept=None):
        df = self.df[self.df['year'] == year]

        if police_dept:
            df = df[df['police_dept'] == police_dept]
        
        fig = px.scatter_mapbox(
            data_frame=df,
            lat='latitude',
            lon='longitude',
            color='category',
            hover_name='address',
            mapbox_style='carto-positron',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='month'
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # daily
    def map_crimes_by_month(self, year, month, police_dept=None):
        if not year:
            return None

        df = self.df[self.df['year'] == year]
        df = df[df['month'] == month]

        if police_dept:
            df = df[df['police_dept'] == police_dept]
        
        fig = px.scatter_mapbox(
            data_frame=df,
            lat='latitude',
            lon='longitude',
            color='category',
            hover_name='address',
            mapbox_style='carto-positron',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='day'
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # hourly
    def map_crimes_by_day(self, year, month, day, police_dept=None):
        if not year:
            return None
    
        if not month:
            return None
    
        df = self.df[self.df['year'] == year]
        df = df[df['month'] == month]
        df = df[df['day'] == day]

        if police_dept:
            df = df[df['police_dept'] == police_dept]

        fig = px.scatter_mapbox(
            data_frame=df,
            lat='latitude',
            lon='longitude',
            color='category',
            hover_name='address',
            mapbox_style='carto-positron',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='hour'
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # map layout
    def _mapper_layout(self, fig):
        fig.update_layout(
            autosize=True,
            height=600,
            hovermode='closest',
            showlegend=True,
            margin=dict(l=10, r=10, t=30, b=0)
        )
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 500
        fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        return fig

#####################################################################

class MapChoropleth:
    def __init__(self, df, gdf):
        self.df = df
        self.gdf = gdf[['district', 'shape_area', 'geometry']]
        self.geojson = self.gdf.__geo_interface__
        self.clat = 37.773972
        self.clon = -122.431297
    
    # yearly
    def map_crimes(self):
        df = self.df.groupby(by=['year', 'police_dept']).count().reset_index()
        df = df[['year', 'police_dept', 'address']]
        df.columns = ['year', 'district', 'cases_reported']
            
        fig = px.choropleth_mapbox(
            data_frame=df,
            geojson=self.geojson,
            locations='district',
            color='cases_reported',
            featureidkey='properties.district',
            mapbox_style='carto-positron',
            color_continuous_scale='Reds',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='year',
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # monthly
    def map_crimes_by_year(self, year):
        df = self.df[self.df['year'] == year]
        
        df = df.groupby(by=['month', 'police_dept']).count().reset_index()
        df = df[['month', 'police_dept', 'address']]
        df.columns = ['month', 'district', 'cases_reported']
            
        fig = px.choropleth_mapbox(
            data_frame=df,
            geojson=self.geojson,
            locations='district',
            color='cases_reported',
            featureidkey='properties.district',
            mapbox_style='carto-positron',
            color_continuous_scale='Reds',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='month',
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # daily
    def map_crimes_by_month(self, year, month):
        if not year:
            return None

        df = self.df[self.df['year'] == year]
        df = df[df['month'] == month]
        
        df = df.groupby(by=['day', 'police_dept']).count().reset_index()
        df = df[['day', 'police_dept', 'address']]
        df.columns = ['day', 'district', 'cases_reported']
            
        fig = px.choropleth_mapbox(
            data_frame=df,
            geojson=self.geojson,
            locations='district',
            color='cases_reported',
            featureidkey='properties.district',
            mapbox_style='carto-positron',
            color_continuous_scale='Reds',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='day',
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # hourly
    def map_crimes_by_day(self, year, month, day):
        if not year:
            return None
    
        if not month:
            return None
    
        df = self.df[self.df['year'] == year]
        df = df[df['month'] == month]
        df = df[df['day'] == day]

        df = df.groupby(by=['hour', 'police_dept']).count().reset_index()
        df = df[['hour', 'police_dept', 'address']]
        df.columns = ['hour', 'district', 'cases_reported']
            
        fig = px.choropleth_mapbox(
            data_frame=df,
            geojson=self.geojson,
            locations='district',
            color='cases_reported',
            featureidkey='properties.district',
            mapbox_style='carto-positron',
            color_continuous_scale='Reds',
            center=dict(lat=self.clat, lon=self.clon),
            zoom=10,
            animation_frame='hour',
        )
        fig = self._mapper_layout(fig=fig)
        fig.show()
        
        return None
    
    # map layout
    def _mapper_layout(self, fig):
        fig.update_layout(
            autosize=True,
            height=600,
            hovermode='closest',
            showlegend=False,
            margin=dict(l=10, r=10, t=30, b=0)
        )
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 500
        fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        return fig

#####################################################################

class OccurrencePlotter:
    def __init__(self, df):
        self.df = df
    
    # yearly
    def plot_crime_occurrences(self, police_dept=None):
        if police_dept:
            df = self.df[self.df['police_dept'] == police_dept]
        else:
            df = self.df

        df = df.groupby(by=['year', 'category']).count().reset_index()
        df = df[['year', 'category', 'address']]
        df.columns = ['year', 'category', 'occurrence']
        
        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            markers=True,
            animation_frame='year'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()
        
        return None
    
    # monthly
    def plot_crime_occurrences_by_year(self, year, police_dept=None):
        df = self.df[self.df['year'] == year]

        if police_dept:
            df = df[df['police_dept'] == police_dept]
        
        df = df.groupby(by=['month', 'category']).count().reset_index()
        df = df[['month', 'category', 'address']]
        df.columns = ['month', 'category', 'occurrence']
        
        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            markers=True,
            animation_frame='month'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()
        
        return None
    
    # daily
    def plot_crime_occurrences_by_month(self, year, month, police_dept=None):
        if not year:
            return None
        
        df = self.df[self.df['year'] == year]
        df = df[df['month'] == month]

        if police_dept:
            df = df[df['police_dept'] == police_dept]
        
        df = df.groupby(by=['day', 'category']).count().reset_index()
        df = df[['day', 'category', 'address']]
        df.columns = ['day', 'category', 'occurrence']
        
        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            markers=True,
            animation_frame='day'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()
        
        return None
    
    # hourly
    def plot_crime_occurrences_by_day(self, year, month, day, police_dept=None):
        if not year:
            return None
    
        if not month:
            return None
        
        df = self.df[self.df['year'] == year]
        df = df[df['month'] == month]
        df = df[df['day'] == day]

        if police_dept:
            df = df[df['police_dept'] == police_dept]
        
        df = df.groupby(by=['hour', 'category']).count().reset_index()
        df = df[['hour', 'category', 'address']]
        df.columns = ['hour', 'category', 'occurrence']
        
        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            markers=True,
            animation_frame='hour'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()
        
        return None
    
    # figure layout
    def _figure_layout(self, fig):
        fig.update_layout(
            autosize=True,
            height=600,
            showlegend=False,
            margin=dict(l=10, r=10, t=30, b=0)
        )
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 500
        fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        return fig

#####################################################################

class CategoryOccurrencePlotter:
    def __init__(self, df):
        self.df = df

    # yearly (month-wise)
    def plot_crime_occurrences_by_month(self):
        df = self.df.groupby(by=['year', 'month', 'category']).count().reset_index()

        df = df[['year', 'month', 'category', 'address']]
        df.columns = ['year', 'month', 'category', 'occurrence']

        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            color='month',
            animation_frame='year'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()

        return None

    # yearly (weekday-wise)
    def plot_crime_occurrences_by_weekday(self):
        df = self.df.groupby(by=['year', 'weekday', 'category']).count().reset_index()
        
        df = df[['year', 'weekday', 'category', 'address']]
        df.columns = ['year', 'weekday', 'category', 'occurrence']

        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            color='weekday',
            animation_frame='year'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()
        
        return None

    # yearly (hour-wise)
    def plot_crime_occurrences_by_hour(self):
        df = self.df.groupby(by=['year', 'hour', 'category']).count().reset_index()
        
        df = df[['year', 'hour', 'category', 'address']]
        df.columns = ['year', 'hour', 'category', 'occurrence']

        fig = px.line(
            data_frame=df,
            x='category',
            y='occurrence',
            color='hour',
            animation_frame='year'
        )
        fig = self._figure_layout(fig=fig)
        fig.show()
        
        return None

    # figure layout
    def _figure_layout(self, fig):
        fig.update_layout(
            autosize=True,
            height=600,
            showlegend=True,
            margin=dict(l=10, r=10, t=30, b=0)
        )
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 500
        fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        return fig

#####################################################################

