select ref.snippet_title, stats.*
from ref_stats stats
join cleansed_stats_ref_data ref on stats.category_id = ref.id;