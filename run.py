import mlflow
import tf_model
import click
import os

@click.command()
@click.option("--tracking-uri", type=click.STRING, default=os.environ['MLFLOW_TRACKING_URI'])
@click.option("--experiment-name", type=click.STRING, default=os.environ['MLFLOW_EXP_NAME'])
@click.option("--model", type=click.STRING, default="1")
@click.option("--config", type=click.STRING, default="0")
@click.option("--model-dir", type=click.STRING, default="")
def run(tracking_uri, experiment_name, model, config, model_dir):
    
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)
    tf_model.run(experiment_name, int(model.strip()), int(config.strip()))

if __name__ == "__main__":

    run()