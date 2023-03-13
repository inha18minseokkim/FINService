package RealEstateDailyJob;

import org.quartz.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.TimeZone;

import static org.quartz.CronScheduleBuilder.cronSchedule;

@Configuration
public class RealEstateDailyExecutor implements Job {

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("ASDF");
    }
    @Bean
    public JobDetail RealEstateDailyDetail() {
        return JobBuilder.newJob().ofType(RealEstateDailyExecutor.class).storeDurably().withIdentity("job_detail")
                .withDescription("Invoke RealEStateDailyExecutor").build();
    }
    @Bean
    public Trigger RealEstateDailyTrigger(@Qualifier("RealEstateDailyDetail") JobDetail job){
        return TriggerBuilder.newTrigger().forJob(job).withIdentity("job_trigger").withSchedule(
                cronSchedule("0 0 9 * * ?").inTimeZone(TimeZone.getTimeZone("Asia/Seoul"))
        ).build();
    }
}

public class