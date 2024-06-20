package khaled.alaya.jwt_demo.repo;

import org.hibernate.mapping.List;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import khaled.alaya.jwt_demo.model.chat;
import khaled.alaya.jwt_demo.model.message;

@Repository
public interface messageRepo extends CrudRepository<message,Long>{

    // Iterable<message> findByChat_id(chat chat_id);
    @Query("SELECT c FROM message c WHERE c.chat_id = :chat")
    java.util.List<message> findmessageByChat(@Param("chat") chat chat);
}
